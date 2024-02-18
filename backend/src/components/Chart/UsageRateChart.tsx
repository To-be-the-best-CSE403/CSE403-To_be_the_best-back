import { BarChart } from "@mantine/charts";

export interface UsageRateData {
  pokemon: string;
  InBattle: number;
  Unused: number;
}

interface UsageRateChartProps {
  data: UsageRateData[];
}

export function UsageRateChart({ data }: UsageRateChartProps) {
  return (
    <BarChart
      h={300}
      data={data}
      dataKey="pokemon"
      type="stacked"
      withTooltip={false}
      orientation="vertical"
      yAxisProps={{ width: 80 }}
      series={[
        { name: "InBattle", color: "blue.6" },
        { name: "Unused", color: "gray.6" },
      ]}
    />
  );
}
