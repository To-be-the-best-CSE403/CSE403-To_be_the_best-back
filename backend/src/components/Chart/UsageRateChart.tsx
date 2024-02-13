import { BarChart } from "@mantine/charts";

interface UsageRateChartProps {
  data: { pokemon: string; usage: number }[];
}

export function UsageRateChart({ data }: UsageRateChartProps) {
  return (
    <BarChart
      h={300}
      data={data}
      dataKey="pokemon"
      type="stacked"
      orientation="vertical"
      yAxisProps={{ width: 80 }}
      series={[{ name: "usage", color: "blue" }]}
    />
  );
}
