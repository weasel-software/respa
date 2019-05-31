from unittest.mock import MagicMock, create_autospec, patch

import pytest
from rest_framework.reverse import reverse

from ..factories import ProductFactory
from ..models import Order
from ..providers.base import PaymentProvider

LIST_URL = reverse('order-list')

ORDER_RESPONSE_FIELDS = {
    'reservation', 'payer_first_name', 'payer_last_name', 'payer_email_address', 'payer_address_street',
    'payer_address_zip', 'payer_address_city', 'id', 'price', 'status', 'order_number', 'payment_url', 'order_lines'
}


def get_detail_url(order):
    return reverse('order-detail', kwargs={'pk': order.pk})


def build_order_data(reservation, product, quantity=None, product_2=None, quantity_2=None):
    data = {
        "reservation": reservation.id,
        "order_lines": [
            {
                "product": product.product_id,
            }
        ],
        "return_url": "https://varauspalvelu.com/payment_return_url/",
        "payer_first_name": "Kalle",
        "payer_last_name": "Nieminen",
        "payer_email_address": "Kalle@nieminen.com",
        "payer_address_street": "Niemitie 5",
        "payer_address_zip": "66666",
        "payer_address_city": "Niemelä"
    }

    if quantity:
        data['order_lines'][0]['quantity'] = quantity

    if product_2:
        order_line_data = {'product': product_2.product_id}
        if quantity_2:
            order_line_data['quantity'] = quantity_2
        data['order_lines'].append(order_line_data)

    return data


@pytest.fixture(autouse=True)
def auto_use_django_db(db):
    pass


@pytest.fixture(autouse=True)
def mock_provider():
    mocked_provider = create_autospec(PaymentProvider)
    mocked_provider.order_create = MagicMock(return_value='https://mocked-payment-url.com')
    with patch('payments.api.get_payment_provider', return_value=mocked_provider):
        yield mocked_provider


@pytest.fixture
def product(resource_in_unit):
    return ProductFactory(resources=[resource_in_unit])


@pytest.fixture
def product_2(resource_in_unit):
    return ProductFactory(resources=[resource_in_unit])


@pytest.fixture
def order_data(two_hour_reservation, product):
    return build_order_data(two_hour_reservation, product)


def test_order_get_list(user_api_client, order_with_products):
    response = user_api_client.get(LIST_URL)

    assert response.status_code == 200
    results = response.data['results']
    assert len(results) == 1
    assert set(results[0].keys()) == ORDER_RESPONSE_FIELDS


def test_order_get_detail(user_api_client, order_with_products):
    response = user_api_client.get(get_detail_url(order_with_products))

    assert response.status_code == 200
    assert set(response.data.keys()) == ORDER_RESPONSE_FIELDS


def test_order_put_forbidden(user_api_client, order_with_products, order_data):
    response = user_api_client.put(get_detail_url(order_with_products), order_data)
    assert response.status_code == 405


def test_order_patch_forbidden(user_api_client, order_with_products, order_data):
    response = user_api_client.patch(get_detail_url(order_with_products), order_data)
    assert response.status_code == 405


def test_order_post(user_api_client, two_hour_reservation, product, product_2, mock_provider):
    order_data = build_order_data(two_hour_reservation, product=product, product_2=product_2, quantity_2=5)

    response = user_api_client.post(LIST_URL, order_data)

    assert response.status_code == 201
    mock_provider.order_create.assert_called()

    # check response fields
    order_create_response_fields = ORDER_RESPONSE_FIELDS.copy() | {'payment_url'}
    assert set(response.data.keys()) == order_create_response_fields
    assert response.data['payment_url'].startswith('https://mocked-payment-url.com')

    # check created object's data
    new_order = Order.objects.last()
    order_fields = {
        'payer_first_name', 'payer_last_name', 'payer_email_address', 'payer_address_street',
        'payer_address_zip', 'payer_address_city'
    }
    for field in order_fields:
        assert getattr(new_order, field) == order_data[field]
    assert new_order.reservation_id == order_data['reservation']

    # check order lines
    order_lines = new_order.order_lines.all()
    assert order_lines.count() == 2
    assert order_lines[0].product == product
    assert order_lines[0].quantity == 1
    assert order_lines[1].product == product_2
    assert order_lines[1].quantity == 5


def test_order_product_must_match_resource(user_api_client, product, two_hour_reservation, resource_in_unit2):
    product_with_another_resource = ProductFactory(resources=[resource_in_unit2])
    order_data = build_order_data(two_hour_reservation, product=product, product_2=product_with_another_resource)

    response = user_api_client.post(LIST_URL, order_data)

    assert response.status_code == 400
    assert 'product' in response.data['order_lines'][1]


def test_order_can_be_created_only_for_own_reservations(api_client, user2, order_data):
    api_client.force_authenticate(user=user2)

    response = api_client.post(LIST_URL, order_data)

    assert response.status_code == 403