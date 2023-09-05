import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Bar } from "react-chartjs-2";
import { React } from "react";

const BarChart = ({ chartData }) => {
  ChartJS.register(ArcElement, Tooltip, Legend);
  return <Bar data={chartData} />;
};

export default BarChart;
