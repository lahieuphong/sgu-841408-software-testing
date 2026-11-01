const getSales = (dateStart, dateEnd, typeDate) => {
  console.log(dateStart, dateEnd, typeDate);
  return $.ajax({
    url:
      "util/statistic.php?dateStart=" +
      dateStart +
      "&dateEnd=" +
      dateEnd +
      "&typeDate=" +
      typeDate +
      "&action=getSales",
    type: "GET",
  });
};
const getNumberOfKindProductsSold = (dateStart, dateEnd) => {
  return $.ajax({
    url:
      "util/statistic.php?dateStart=" +
      dateStart +
      "&dateEnd=" +
      dateEnd +
      "&action=getNumberOfKindProductsSold",
    type: "GET",
  });
};
const getNumberOfProductsSold = (dateStart, dateEnd) => {
  return $.ajax({
    url:
      "util/statistic.php?dateStart=" +
      dateStart +
      "&dateEnd=" +
      dateEnd +
      "&action=getNumberOfProductsSold",
    type: "GET",
  });
};

const getTopKindProducts = (dateStart, dateEnd, limit) => {
  return $.ajax({
    url:
      "util/statistic.php?dateStart=" +
      dateStart +
      "&dateEnd=" +
      dateEnd +
      "&limit=" +
      limit +
      "&action=getTopKindProducts",
    type: "GET",
  });
};

const getTopProducts = (dateStart, dateEnd, limit) => {
  return $.ajax({
    url:
      "util/statistic.php?dateStart=" +
      dateStart +
      "&dateEnd=" +
      dateEnd +
      "&limit=" +
      limit +
      "&action=getTopProducts",
    type: "GET",
  });
};
const changeTypeInputDate = () => {
  let dateStartInput = document.querySelector("#statistic-type1 .dateStart");
  let dateEndInput = document.querySelector("#statistic-type1 .dateEnd");
  dateStartInput.value = "";
  dateEndInput.value = "";
  let typeInput = document.querySelector("#statistic-type1 .typeStatictis");
  if (typeInput.value == "1") {
    dateStartInput.type = "text";
    dateEndInput.type = "text";
  } else if (typeInput.value == "2") {
    dateStartInput.type = "month";
    dateEndInput.type = "month";
  } else if (typeInput.value == "3") {
    dateStartInput.type = "week";
    dateEndInput.type = "week";
  } else {
    dateStartInput.type = "date";
    dateEndInput.type = "date";
    console.log("y");
  }
};
Date.prototype.getWeek = function () {
  let date = new Date(this.getTime());
  date.setHours(0, 0, 0, 0);
  date.setDate(date.getDate() + 4 - (date.getDay() || 7));
  let yearStart = new Date(date.getFullYear(), 0, 1);
  let weekNo = Math.ceil(((date - yearStart) / 86400000 + 1) / 7);
  return weekNo;
};

const checkInputStatistic1 = () => {
  let dateStartInput = document.querySelector("#statistic-type1 .dateStart");
  let dateEndInput = document.querySelector("#statistic-type1 .dateEnd");
  let typeInput = document.querySelector("#statistic-type1 .typeStatictis");
  if (dateStartInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter date start!",
      3
    );
    dateStartInput.focus();
    return false;
  }
  if (dateEndInput.value == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter date end!",
      3
    );
    dateEndInput.focus();
    return false;
  }
  let currentDate = new Date();
  switch (typeInput.value) {
    case "1":
      yearStart = dateStartInput.value;
      yearEnd = dateEndInput.value;
      if (isNaN(yearStart)) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Year start must be a number!",
          3
        );
        dateStartInput.focus();
        return false;
      }
      if (isNaN(yearEnd)) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Year end must be a number!",
          3
        );
        dateEndInput.focus();
        return false;
      }
      if (parseInt(yearStart) < 2000) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Year start must greater than 2000!",
          3
        );
        dateEndInput.focus();
        return false;
      }
      if (parseInt(yearEnd) < 2000) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Year end must greater than 2000!",
          3
        );
        dateEndInput.focus();
        return false;
      }
      if (parseInt(yearEnd) > new Date().getFullYear()) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Year end must be less than or equal current year!",
          3
        );
        dateEndInput.focus();
        return false;
      }
      if (parseInt(yearStart) > parseInt(yearEnd)) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Year start must be less than or equal year end!",
          3
        );
        dateStartInput.focus();
        return false;
      }
      break;
    case "2":
      monthStart = dateStartInput.value;
      monthEnd = dateEndInput.value;
      if (monthEnd > new Date().toISOString().slice(0, 7)) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Month end must be less than or equal current month!",
          3
        );
        dateEndInput.focus();
        return false;
      }
      if (monthStart > monthEnd) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Month start must be less than or equal month end!",
          3
        );
        dateStartInput.focus();
        return false;
      }
      break;
    case "3":
      weekStart = dateStartInput.value;
      weekEnd = dateEndInput.value;
      let currentYear = currentDate.getFullYear();
      let currentWeek = currentDate.getWeek();
      let weekEndYear = parseInt(weekEnd.substring(0, 4));
      let weekEndWeek = parseInt(weekEnd.substring(6));
      let weekStartYear = parseInt(weekStart.substring(0, 4));
      let weekStartWeek = parseInt(weekStart.substring(6));
      if (
        weekEndYear > currentYear ||
        (currentYear === weekEndYear && weekEndWeek > currentWeek)
      ) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Week end must be less than or equal current week!",
          3
        );
        dateEndInput.focus();
        return false;
      }
      if (
        weekStartYear > weekEndYear ||
        (weekStartYear === weekEndYear && weekStartWeek > weekEndWeek)
      ) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Week start must be less than or equal week end!",
          3
        );
        dateEndInput.focus();
        return false;
      }
    case "4":
      dateStart = dateStartInput.value;
      dateEnd = dateEndInput.value;
      currentDate.setDate(currentDate.getDate() + 1);
      if (new Date(dateEnd) > currentDate) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Date end must be less than or equal current date!",
          3
        );
        dateEndInput.focus();
        return false;
      }
      if (new Date(dateStart) > new Date(dateEnd)) {
        customNotice(
          "fa-sharp fa-light fa-circle-exclamation",
          "Date start must be less than or equal date end!",
          3
        );
        dateEndInput.focus();
        return false;
      }
      break;
  }
  return true;
};
const statistic1 = async () => {
  if (!checkInputStatistic1()) return;
  let dateStartInput = document.querySelector("#statistic-type1 .dateStart");
  let dateEndInput = document.querySelector("#statistic-type1 .dateEnd");
  let typeInput = document.querySelector("#statistic-type1 .typeStatictis");
  let data = JSON.parse(
    await getSales(dateStartInput.value, dateEndInput.value, typeInput.value)
  );
  console.log(data);
  let categories = [];
  let formattedData;
  let title;
  let nameLine;
  switch (typeInput.value) {
    case "1": //year
      yearStart = parseInt(dateStartInput.value);
      yearEnd = parseInt(dateEndInput.value);
      for (let year = yearStart; year <= yearEnd; year++) {
        categories.push(year + "");
      }
      formattedData = categories.map((year) => {
        const existingData = data.find((item) => item.y === year);
        const total = existingData ? parseInt(existingData.total) : 0;
        return { year, total };
      });
      title = "Sales revenue from " + yearStart + " to " + yearEnd;
      nameLine = yearStart + "-" + yearEnd;
      break;
    case "2": //month
      monthStart = dateStartInput.value;
      monthEnd = dateEndInput.value;
      let startDateMonth = new Date(monthStart + "-01");
      let endDateMonth = new Date(monthEnd + "-01");
      while (startDateMonth <= endDateMonth) {
        let formattedDate = startDateMonth.toISOString().slice(0, 7);
        categories.push(formattedDate);
        startDateMonth.setMonth(startDateMonth.getMonth() + 1);
      }
      formattedData = categories.map((month) => {
        const existingData = data.find((item) => item.m === month);
        const total = existingData ? parseInt(existingData.total) : 0;
        return { month, total };
      });
      categories = categories.map((month) =>
        month.split("-").reverse().join("/")
      );
      monthStartDisplay = monthStart.split("-").reverse().join("/");
      monthEndDisplay = monthEnd.split("-").reverse().join("/");
      title =
        "Sales revenue from " + monthStartDisplay + " to " + monthEndDisplay;
      nameLine = monthStartDisplay + " - " + monthEndDisplay;
      break;
    case "3":
      weekStart = dateStartInput.value;
      weekEnd = dateEndInput.value;
      let startYear = parseInt(weekStart.substring(0, 4));
      let endYear = parseInt(weekEnd.substring(0, 4));
      let startNum = parseInt(weekStart.substring(6));
      let endNum = parseInt(weekEnd.substring(6));
      for (let year = startYear; year <= endYear; year++) {
        let start = year === startYear ? startNum : 1;
        let end = year === endYear ? endNum : 52;
        for (let week = start; week <= end; week++) {
          let weekString = year + "-" + String(week).padStart(2, "0");
          categories.push(weekString);
        }
      }
      formattedData = categories.map((week) => {
        const existingData = data.find((item) => item.w === week);
        const total = existingData ? parseInt(existingData.total) : 0;
        return { week, total };
      });
      categories = categories.map(
        (week) => week.slice(0, 5) + "W" + week.slice(5)
      );
      title = "Sales revenue from " + weekStart + " to " + weekEnd;
      nameLine = weekStart + " - " + weekEnd;
      break;
    case "4":
      dateStart = dateStartInput.value;
      dateEnd = dateEndInput.value;
      startDate = new Date(dateStart);
      endDate = new Date(dateEnd);
      while (startDate <= endDate) {
        const formattedDate = startDate.toISOString().split("T")[0];
        categories.push(formattedDate);
        startDate.setDate(startDate.getDate() + 1);
      }
      formattedData = categories.map((date) => {
        const existingData = data.find((item) => item.d === date);
        const total = existingData ? parseInt(existingData.total) : 0;
        return { date, total };
      });
      categories = categories.map((date) =>
        date.split("-").reverse().join("/")
      );
      dateStartDisplay = dateStart.split("-").reverse().join("/");
      dateEndDisplay = dateEnd.split("-").reverse().join("/");
      title =
        "Sales revenue from " + dateStartDisplay + " to " + dateEndDisplay;
      nameLine = dateStartDisplay + " - " + dateEndDisplay;
      break;
  }
  Highcharts.chart("container", {
    chart: {
      type: "line",
    },
    title: {
      text: title,
    },
    xAxis: {
      categories: categories,
    },
    yAxis: {
      title: {
        text: "Total sales revenue",
      },
    },
    plotOptions: {
      series: {
        color: "#f2623e",
      },
      line: {
        dataLabels: {
          enabled: true,
        },
        enableMouseTracking: false,
      },
    },
    series: [
      {
        name: nameLine,
        data: formattedData.map((item) => item.total),
      },
    ],
  });
};

const statistic2 = async () => {
  let dateStart = document.querySelector("#statistic-type2 .dateStart").value;
  let dateEnd = document.querySelector("#statistic-type2 .dateEnd").value;
  if (dateStart == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter date start!",
      3
    );
    return;
  }
  if (dateEnd == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter date end!",
      3
    );
    return;
  }
  if (new Date(dateStart) > new Date(dateEnd)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Date start must be smaller or equal date end!",
      3
    );
    return;
  }
  let typeInput = document.querySelector("#statistic-type2 .typeStatictis");
  let data;
  if (typeInput.value == "1") {
    data = JSON.parse(await getNumberOfKindProductsSold(dateStart, dateEnd));
  } else if (typeInput.value == "2") {
    data = JSON.parse(await getNumberOfProductsSold(dateStart, dateEnd));
  }

  let dataFormat = data.map((obj) => [obj.ten, parseInt(obj.soLuong)]);

  let title;
  let date =
    dateStart.split("-").reverse().join("/") +
    " to " +
    dateEnd.split("-").reverse().join("/");
  if (typeInput.value == "1") {
    title = "Number of products sold by product type from " + date;
  } else {
    title = "Number of products sold from " + date;
  }
  Highcharts.chart("container2", {
    chart: {
      type: "column",
    },
    title: {
      text: title,
    },
    xAxis: {
      type: "category",
      labels: {
        rotation: -45,
        style: {
          fontSize: "13px",
          fontFamily: "Verdana, sans-serif",
        },
      },
    },
    yAxis: {
      min: 0,
      title: {
        text: "Number of products sold",
      },
    },
    legend: {
      enabled: false,
    },
    tooltip: {
      pointFormat: "<b>{point.y} vinyl records</b>",
    },
    series: [
      {
        name: "Population",
        colors: ["#f2623e"],
        colorByPoint: true,
        groupPadding: 0,
        data: dataFormat,
        dataLabels: {
          enabled: true,
          rotation: -90,
          color: "#FFFFFF",
          align: "right",
          // format: "{point.y:.1f}", // one decimal
          y: 10, // 10 pixels down from the top
          style: {
            fontSize: "13px",
            fontFamily: "Verdana, sans-serif",
          },
        },
      },
    ],
  });
};

const statistic3 = async () => {
  let dateStart = document.querySelector("#statistic-type3 .dateStart").value;
  let dateEnd = document.querySelector("#statistic-type3 .dateEnd").value;
  let limit = document.querySelector("#statistic-type3 .limit").value;
  if (dateStart == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter date start!",
      3
    );
    return;
  }
  if (dateEnd == "") {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Please, enter date end!",
      3
    );
    return;
  }
  if (new Date(dateStart) > new Date(dateEnd)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Date start must be smaller or equal date end!",
      3
    );
    return;
  }
  if (isNaN(limit)) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Limit must be a number",
      3
    );
    return;
  }
  if (parseInt(limit) <= 0) {
    customNotice(
      "fa-sharp fa-light fa-circle-exclamation",
      "Limit must be greater than 0",
      3
    );
    return;
  }
  let typeInput = document.querySelector("#statistic-type3 .typeStatictis");
  let data;
  if (typeInput.value == "1") {
    data = JSON.parse(await getTopKindProducts(dateStart, dateEnd, limit));
  } else if (typeInput.value == "2") {
    data = JSON.parse(await getTopProducts(dateStart, dateEnd, limit));
  }
  let title;
  let date =
    dateStart.split("-").reverse().join("/") +
    " to " +
    dateEnd.split("-").reverse().join("/");
  if (typeInput.value == "1") {
    title = "Top " + limit + " best-selling category from " + date;
  } else {
    title = "Top " + limit + " best-selling product from " + date;
  }
  Highcharts.chart("container3", {
    chart: {
      type: "bar",
    },
    title: {
      text: title,
      align: "left",
    },
    xAxis: {
      categories: data.map((obj) => obj.ten),
      title: {
        text: null,
      },
      gridLineWidth: 1,
      lineWidth: 0,
    },
    yAxis: {
      min: 0,
      title: {
        text: "Number of products sold",
        align: "high",
      },
      labels: {
        overflow: "justify",
      },
      gridLineWidth: 0,
    },
    tooltip: {
      valueSuffix: "vinyl records",
    },
    plotOptions: {
      series: {
        color: "#f2623e",
      },
      bar: {
        borderRadius: "50%",
        dataLabels: {
          enabled: true,
        },
        groupPadding: 0.1,
      },
    },
    legend: {
      layout: "vertical",
      align: "right",
      verticalAlign: "bottom",
      x: -40,
      y: 80,
      floating: true,
      borderWidth: 1,
      backgroundColor:
        Highcharts.defaultOptions.legend.backgroundColor || "#FFFFFF",
      shadow: true,
    },
    credits: {
      enabled: false,
    },
    series: [
      {
        name: "",
        data: data.map((obj) => parseInt(obj.soLuong)),
      },
    ],
  });
};

module.exports = {
  getSales,
  getNumberOfKindProductsSold,
  getNumberOfProductsSold,
  getTopKindProducts,
  getTopProducts,
  changeTypeInputDate,
  checkInputStatistic1,
  statistic1,
  statistic2,
  statistic3,
};