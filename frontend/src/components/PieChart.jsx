import { Pie } from "react-chartjs-2";
import { React } from "react";
import { Chart as ChartJS } from "chart.js/auto";

const PieChart = ({ chartData }) => {
  console.log(chartData);
  return <Pie data={chartData} />;
};

export default PieChart;
