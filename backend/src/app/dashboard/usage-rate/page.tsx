"use client";

import { useEffect, useState } from "react";
import { UsageRateChart } from "@/components/Chart/UsageRateChart";

interface UsageRateData {
  pokemon: string;
  usage: number;
}

export default function UsageRate() {
  const [usageRateData, setUsageRateData] = useState<UsageRateData[]>([]);
  const n = 10;

  useEffect(() => {
    const fetchUsageRateData = async () => {
      try {
        const response = await fetch(
          `https://tobethebest.vercel.app/api/usage-rate?n=${n}`
        );
        const data = await response.json();
        const usage = data.map((tuple: any) => {
          const [_, pokemon, usage] = tuple;
          return { pokemon: pokemon, usage: usage };
        });
        console.log("Fetching usage rate data:", usage);
        setUsageRateData(usage);
      } catch (error) {
        console.error("Error fetching usage rate data:", error);
      }
    };
    fetchUsageRateData();
  }, [n]);

  return (
    <div>
      <h1>Usage Rate</h1>
      <h2>Top 10 Most Used Pokemon</h2>
      <UsageRateChart data={usageRateData} />
    </div>
  );
}
