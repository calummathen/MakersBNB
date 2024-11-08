


flatpickr("#inlineCalendar", {
    inline: true, 
    altInput: true,
    altFormat: "F j, Y",
    dateFormat: "Y-m-d",
    shorthandCurrentMonth: true,
    minDate: "today",
    maxDate: new Date().fp_incr(180),
    disable: unavailableDates,
    mode: "range",

    onReady: function(selectedDates, dateStr, instance) {
        reapplyStyles(instance);
    },
    onMonthChange: function(selectedDates, dateStr, instance) {
        reapplyStyles(instance);
    },
    onYearChange: function(selectedDates, dateStr, instance) {
        reapplyStyles(instance);
    },

    onChange: function(selectedDates, dateStr, instance) {
        reapplyStyles(instance)
        const [startDate, endDate] = dateStr.split(" to ");
        document.getElementById("startDate").value = startDate;
        document.getElementById("endDate").value = endDate; 
        const start = new Date(startDate);
        const end = new Date(endDate);
        
        const differenceInTime = end.getTime() - start.getTime();
        let totalPrice = 0;
        let differenceInDays = 0;
        if (!isNaN(differenceInTime)) {
            differenceInDays = differenceInTime / (1000 * 3600 * 24);
            totalPrice = differenceInDays * pricePerNight
        }
        
        document.getElementById("totalDays").textContent = "Number of days: " + differenceInDays;
        document.getElementById("totalDays").textContent = "Total price: £" + totalPrice + " for " + differenceInDays + " nights";
        // document.getElementById("selectedDates").textContent = "Selected Date: " + dateStr;
    }
});

function reapplyStyles(instance) {
    unavailableDates.forEach(range => {
        // Format the dates to match the aria-label format (e.g., "November 6, 2024")
        const startDate = new Date(range.from).toLocaleDateString('en-US', {
            month: 'long', 
            day: 'numeric', 
            year: 'numeric' 
        });

        const endDate = new Date(range.to).toLocaleDateString('en-US', {
            month: 'long',
            day: 'numeric',
            year: 'numeric'
        });

        // Calculate the day before the start and the day after the end
        const dayBeforeStart = new Date(range.from);
        dayBeforeStart.setDate(dayBeforeStart.getDate() - 1);

        const dayAfterEnd = new Date(range.to);
        dayAfterEnd.setDate(dayAfterEnd.getDate() + 1);

        const prevStartDate = dayBeforeStart.toLocaleDateString('en-US', {
            month: 'long',
            day: 'numeric',
            year: 'numeric'
        });

        const nextEndDate = dayAfterEnd.toLocaleDateString('en-US', {
            month: 'long',
            day: 'numeric',
            year: 'numeric'
        });

        // Find the days in the calendar for the range
        const startDay = instance.calendarContainer.querySelector(`.flatpickr-day[aria-label="${startDate}"]`);
        const endDay = instance.calendarContainer.querySelector(`.flatpickr-day[aria-label="${endDate}"]`);
        const prevStartDay = instance.calendarContainer.querySelector(`.flatpickr-day[aria-label="${prevStartDate}"]`);
        const nextEndDay = instance.calendarContainer.querySelector(`.flatpickr-day[aria-label="${nextEndDate}"]`);

        if (prevStartDay) prevStartDay.classList.add('start-day-prev');
        if (nextEndDay) nextEndDay.classList.add('end-day-next');
        if (startDay) startDay.classList.add('start-day');
        if (endDay) endDay.classList.add('end-day');
    });
}
