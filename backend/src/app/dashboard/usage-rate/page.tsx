"use client";

import { useEffect, useState } from "react";
import { Container } from "@mantine/core";
import { UsageTopChart, UsageTopData } from "@/components/Chart/UsageTopChart";
import { API_ENDPOINTS } from "@/api";

export default function UsageRate() {
  const [usageTopData, setUsageTopData] = useState<UsageTopData[]>([]);
  const n = 10;

  useEffect(() => {
    const fetchUsageTopData = async () => {
      try {
        const response = await fetch(`${API_ENDPOINTS.USAGE_TOP}?n=${n}`);
        const data = await response.json();
        const usage = data.map((d: any) => ({
          pokemon: d.name,
          InBattle: d.raw_count,
          Unused: d.raw_count - d.real_count,
        }));
        console.log("usage", usage);
        setUsageTopData(usage);
      } catch (error) {
        console.error("Error fetching usage top data:", error);
      }
    };
    fetchUsageTopData();
  }, [n]);

  return (
    <Container size="lg">
      <h1>Usage Rate</h1>
      <h2>Top 10 Most Used Pokemon in January 2024</h2>
      <UsageTopChart data={usageTopData} />
    </Container>
  );
}
