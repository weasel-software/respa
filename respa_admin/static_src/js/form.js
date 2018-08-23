let emptyDayItem = null;

/*
* Update the indices of the inputs in the period
* input boxes.
* */
function updatePeriodIndices() {
  let $periods = $('#current-periods-list').children();

  $periods.each(function (rowId, row) {
    let $periodRow = $(row).find('#period-list');
    let periodInput = $periodRow.children();
    let dateInputs = periodInput.find('[id*="date-inputs-"]');
    let idPeriod = row.children[0]; //This is the hidden ID for each period item.
    let idResourcePeriod = row.children[1]; //This is the hidden ID for each period item.

    //Update the hidden period ID to its corresponding row value.
    $(idPeriod).attr('id', $(idPeriod).attr('id').replace(/-(\d+)-/, "-" + rowId + "-"));
    $(idPeriod).attr('name', $(idPeriod).attr('name').replace(/-(\d+)-/, "-" + rowId + "-"));

    //Update the hidden resource ID to its corresponding row value.
    $(idResourcePeriod).attr('id', $(idResourcePeriod).attr('id').replace(/-(\d+)-/, "-" + rowId + "-"));
    $(idResourcePeriod).attr('name', $(idResourcePeriod).attr('name').replace(/-(\d+)-/, "-" + rowId + "-"));

    // Update the input ids of the divs containing period inputs and date inputs as well.
    $(periodInput).attr('id', $(periodInput).attr('id').replace(/-(\d+)/, "-" + rowId));
    $(dateInputs).attr('id', $(dateInputs).attr('id').replace(/-(\d+)/, "-" + rowId));

    //Update the name, start and end input ids.
    $periodRow.children().each(function (cellIndex, cell) {
      let $inputCells = $(cell).find('input');

      $inputCells.each(function (cellIndex, cell) {
        $(cell).attr('id', $(cell).attr('id').replace(/-(\d+)-/, "-" + rowId + "-"));
        $(cell).attr('name', $(cell).attr('name').replace(/-(\d+)-/, "-" + rowId + "-"));
      })
    });
  });
}

/*
* Updates the indices of the various input boxes
* in the each day under a specific period.
*
* param: periodIdNmber (ex the integer from a collapse div or accordion div).
* */
function updateDaysIndices(periodIdNumber) {
  let daysList = $('#collapse' + periodIdNumber).find('#period-days-list');

  daysList.children().each(function (dayIndex, day) {
    $(day).attr('id', $(day).attr('id').replace(/-(\d+)-(\d+)/, '-' + periodIdNumber + '-' + dayIndex));

    $(day).each(function (inputIndex, inputRow) {
      let $inputCells = $(inputRow).find('input');
      let $selectCells = $(inputRow).find('select');

      $inputCells.each(function (cellIndex, cellInput) {
        $(cellInput).attr('id', $(cellInput).attr('id').replace(/-(\d+)-(\d+)-/, '-' + periodIdNumber + '-' + dayIndex + '-'));
        $(cellInput).attr('name', $(cellInput).attr('name').replace(/-(\d+)-(\d+)-/, '-' + periodIdNumber + '-' + dayIndex + '-'));
      });

      $selectCells.each(function (cellIndex, cellInput) {
        $(cellInput).attr('id', $(cellInput).attr('id').replace(/-(\d+)-(\d+)-/, '-' + periodIdNumber + '-' + dayIndex + '-'));
        $(cellInput).attr('name', $(cellInput).attr('name').replace(/-(\d+)-(\d+)-/, '-' + periodIdNumber + '-' + dayIndex + '-'));
      });
    })
  });
}

/*
* Update the indices in the management form of the days
* to match the current period.
* */
function updateDaysMgmtFormIndices(periodId) {
  let $collapseItem = $('#collapse' + periodId);
  let $managementFormInputs = $($collapseItem).find('#days-management-form').find('input');

  $managementFormInputs.each(function (id, input) {
    $(input).attr('id', $(input).attr('id').replace(/id_days-periods-(\d+)-/, 'id_days-periods-' + periodId + '-'));
    $(input).attr('name', $(input).attr('name').replace(/days-periods-(\d+)-/, 'days-periods-' + periodId + '-'));
  });
}

/*
* General function for restoring the values in the
* management form for the days in a period.
* */
function restoreDaysMgmtFormValues(periodId) {
  $("#id_days-periods-" + periodId + "-TOTAL_FORMS").val("0");
  $("#id_days-periods-" + periodId + "-INITIAL_FORMS").val("0");
  $("#id_days-periods-" + periodId + "-MAX_NUM_FORMS").val("1000");
  $("#id_days-periods-" + periodId + "-MIN_NUM_FORMS").val("0");
}

/*
* Update the TOTAL_FORMS value in the management form of the days
* in the corresponding period.
* */
function updateTotalDays(periodIdNumber) {
  let $collapseItem = $('#collapse' + periodIdNumber);
  let $periodDaysList = $collapseItem.find('#period-days-list');

  $($collapseItem).find('#id_days-periods-' + periodIdNumber + '-TOTAL_FORMS').val($periodDaysList[0].childElementCount);
}

/*
* Returns the day values from dates between the dates.
* ret: array of integers.
* */
function getDayValuesInterval(dateArray) {
  let days = [];

  for (let i = 0; i < dateArray.length; i++) {

    let day = dateArray[i].getDay();

    //The Javascript getDays() function's output does not correspond
    //to the Django models weekday choices. Therefore this little hack
    //was introduced.
    if (day === 0) {
      day = 6;
    } else {
      day--;
    }

    days.push(day.toString());
  }

  if (days.length <= 7) {
    return days;
  }

  //Return array without duplicate values.
  return Array.from(new Set(days));
}

/*
* Gets a list of dates between the given date inputs.
* */
function getDateInterval(startDate, endDate) {
  let dateArray = [];

  while (startDate <= endDate) {
    dateArray.push(new Date(startDate));
    startDate.setDate(startDate.getDate() + 1);
  }

  return dateArray;
}

/*
* Handle either removing or adding new days based
* on the date input fields.
* */
function modifyCurrentDays(dates) {
  let periodIdNum = dates.id.match(/[0-9]+/)[0];
  let $daysList = $('#collapse' + periodIdNum).find('#period-days-list');
  let dateInputs = dates.getElementsByTagName('input');
  let $currentWeekdayObjects = $daysList.children().find("[id*='-weekday']");
  let startDate = new Date(dateInputs[0].value);
  let endDate = new Date(dateInputs[1].value);
  let currentDays = [];

  if ((!startDate || !endDate) || (startDate > endDate)) {
    return;
  }

  for (let i = 0; i < $currentWeekdayObjects.length; i++) {
    currentDays.push($currentWeekdayObjects[i].value.toString());
  }

  let newDays = getDayValuesInterval(getDateInterval(startDate, endDate));

  //If a value exists in newDays but not in currentDays => it is a new day to be added.
  for (let i  = 0; i < newDays.length; i++) {
    if (!currentDays.includes(newDays[i])) {
      addDay(periodIdNum, newDays[i]);
    }
  }

  //If a value does not exist in newDays but it does exist in currentDays => remove it.
  for (let i = 0; i < currentDays.length; i++) {
    if (!newDays.includes(currentDays[i])) {
      removeDay(periodIdNum, i);
    }
  }

  updateDaysIndices(periodIdNum);
  updateTotalDays(periodIdNum);
}

/*
* Helper function for modifyDays(). Removes a day
* by creating the exact ID of a day.
* */
function removeDay(periodId, index) {
  $('#period-day-' + periodId + '-' + index).remove();
}

/*
* Add a new day to the period with the integer part of the ID
* and the integer representation of a weekday.
* */
function addDay(periodIdNum, weekday) {
  let $collapseItem = $('#collapse' + periodIdNum);
  let $daysList = $collapseItem.find('#period-days-list');
  let newDayItem = emptyDayItem.clone();

  newDayItem.find("[id*='-weekday']").val(weekday);
  $daysList.append(newDayItem);
}

/*
* Strip all of the input values in a day.
* */
function resetDayInputs(dayItem) {
  let $inputs = dayItem.find(':input');

  for (let i = 0; i < $inputs.length; i++) {
    $inputs[i].value = '';
  }
}

/*
* Strips a period of its input values and days.
* */
function removePeriodInputValues(periodItem, idNum) {
  //Get the inputs to remove (user inputs only).
  $('#id_periods-' + idNum + '-name').val('');
  $('#id_periods-' + idNum + '-start').val('');
  $('#id_periods-' + idNum + '-end').val('');

  //If there's an id_periods value, reset that one as well (used in the edit view).
  $('#id_periods-' + idNum + '-id').removeAttr('value');

  //Remove all days.
  let periodItemDays = periodItem.find('#period-days-list').children();
  for (let i = 0; i < periodItemDays.length; i++) {
    periodItemDays[i].remove();
  }

  //Restore the values in the days management form in this period.
  restoreDaysMgmtFormValues(idNum);
}

/*
* Adds a new period item and updates all the ids where necessary.
* */
function addNewPeriod() {
  // Get the list or periods.
  let $periodList = $('#current-periods-list');

  // Get the first item.
  let $firstAccordionItem = $('#accordion-item-0');

  if ($firstAccordionItem) {
    let newItem = $firstAccordionItem.clone();
    let idNum = $periodList[0].childElementCount;
    const newIdNum = $periodList[0].childElementCount;

    $periodList.append(newItem);

    newItem.attr('id', `accordion-item-${newIdNum}`);
    newItem.find('.dropdown-time').attr('id', `accordion${newIdNum}`);
    newItem.find('.panel-heading').attr({
      id: `heading${newIdNum}`
    });
    newItem.find('.panel-heading a').attr({
      href: `#collapse${newIdNum}`,
      "aria-controls": `#collapse${newIdNum}`
    });
    newItem.find('.panel-collapse').attr({
      "aria-labelledby": `heading${newIdNum}`,
      id: `collapse${newIdNum}`
    });

    //Attach event handler for removing a period (these are not cloned by default).
    newItem.find('button.delete-time').attr('id', `remove-hour-${newIdNum}`);
    newItem.find('button.delete-time').click(() => removeHourHandler(newIdNum));

    updateDaysMgmtFormIndices(newIdNum);
    updatePeriodIndices();
    removePeriodInputValues(newItem, idNum);
    updatePeriodsTotalForms();

    //Attach the event handler for the date pickers.
    let $dates = newItem.find('#date-inputs-' + idNum);
    $dates.change(() => modifyCurrentDays($dates[0]));
  }
}

function updatePeriodsTotalForms() {
  document.getElementById('id_periods-TOTAL_FORMS').value =
    document.getElementById('current-periods-list').childElementCount;
}

/*************************************
* Export functions go here.
**************************************/

/*
* Bind the event handler for closing notification to the elements (buttons)
* since we cant do it directly in the html because of the scope
* */
export function enableNotificationHandler() {
  let notifications = document.getElementsByClassName('noti');
  Array.prototype.forEach.call(notifications, (noti) => {
    noti.getElementsByTagName('button')[0].addEventListener('click', () => noti.remove(), false);
  });
}

/*
* Copy the first day value into a variable and keep it for cloning purposes.
* */
export function copyInitialDay() {
  //Get the first day from the list.
  let $firstCollapseItem = $('#collapse0');
  let $firstDayItem = $firstCollapseItem.find('#period-days-list :first');
  let firstDayDbIds = $firstCollapseItem.find('#day-db-ids').children();

  let weekday = $('#id_days-periods-0-0-weekday').val();
  let opens = $('#id_days-periods-0-0-opens').val();
  let closes = $('#id_days-periods-0-0-closes').val();

  //Clone the served day item into a variable.
  emptyDayItem = $firstDayItem.clone();


  //If none of the following inputs are present, remove the first item
  //because it is an empty initial item served by Django. If some of the
  //inputs are present, it is either an "in progress" day or an item
  //served from the Database.
  if (!firstDayDbIds[0].value && !firstDayDbIds[1].value) {
    if (!weekday && !opens && !closes) {
      $firstDayItem.remove();
    }
  }

  resetDayInputs(emptyDayItem);
  updateTotalDays(0);
}

/*
* Bind event for adding a new period to its corresponding button.
* */
export function enableAddNewPeriod() {
  let button = document.getElementById('add-new-hour');
  button.addEventListener('click', addNewPeriod, false);
}

/*
* Bind event for removing a period to its corresponding button.
* */
export function enableRemovePeriod() {
  let buttons = document.getElementsByClassName('delete-time');
  Array.prototype.forEach.call(buttons, (button) => {
    let periodIdNum = button.id.match(/[0-9]+/)[0];
    button.addEventListener('click', () => removeHourHandler(periodIdNum), false);
  });
}

/*
* Event handler to remove an hour accordion item
* take the Id of that arcordion-item as argument.
**/
export function removeHourHandler(id) {
  let hourItem = document.getElementById(`accordion-item-${id}`);
  hourItem.remove();
  updatePeriodIndices();
  updatePeriodsTotalForms();
}

/*
* Bind event for adding days to the date input fields.
* */
export function enableAddDaysByDate() {
  let periods = document.getElementById('current-periods-list').children;

  for (let i = 0; i < periods.length; i++) {
    let inputDates = document.getElementById('date-inputs-' + i);
    inputDates.addEventListener('change', () => modifyCurrentDays(inputDates), false);
  }
}
