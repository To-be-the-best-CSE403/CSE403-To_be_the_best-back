"use client";

import { useEffect, useState } from "react";
import { Container } from "@mantine/core";
import {
  UsageRateChart,
  UsageRateData,
} from "@/components/Chart/UsageRateChart";
import { API_ENDPOINTS } from "@/api";

export default function UsageRate() {
  const [usageRateData, setUsageRateData] = useState<UsageRateData[]>([]);
  const n = 10;

  useEffect(() => {
    const fetchUsageRateData = async () => {
      try {
        const response = await fetch(`${API_ENDPOINTS.USAGE_TOP}?n=${n}`);
        const data = await response.json();
        const usage = data.map((d: any) => ({
          pokemon: d.name,
          InBattle: d.raw_count,
          Unused: d.raw_count - d.real_count,
        }));
        console.log("usage", usage);
        setUsageRateData(usage);
      } catch (error) {
        console.error("Error fetching usage rate data:", error);
      }
    };
    fetchUsageRateData();
  }, [n]);

  return (
    <Container size="lg">
      <h1>Usage Rate</h1>
      <h2>Top 10 Most Used Pokemon in January 2024</h2>
      <UsageRateChart data={usageRateData} />
    </Container>
  );
}
