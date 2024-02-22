import { BarChart } from "@mantine/charts";

export interface UsageTopData {
  pokemon: string;
  InBattle: number;
  Unused: number;
}

interface UsageTopChartProps {
  data: UsageTopData[];
}

export function UsageTopChart({ data }: UsageTopChartProps) {
  return (
    <BarChart
      h={300}
      data={data}
      dataKey="pokemon"
      type="stacked"
      orientation="vertical"
      yAxisProps={{ width: 80 }}
      series={[
        { name: "InBattle", color: "blue.6" },
        { name: "Unused", color: "gray.6" },
      ]}
    />
  );
}
