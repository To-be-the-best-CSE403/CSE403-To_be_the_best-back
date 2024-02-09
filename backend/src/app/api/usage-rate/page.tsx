"use client";

import React from "react";
import UsageRateMdx from "./usage-rate.mdx";
import BarChart from '@mantine/charts';
import data from './temp_data';

export default function UsageRate() {
  return (
    <div>
      <UsageRateMdx />
        <BarChart
            h={300}
            data={data}
            dataKey="pokemon"
            series={[
                { name: 'Usage rate (%)', color: 'violet.6' }
                // { name: 'Laptops', color: 'blue.6' },
                // { name: 'Tablets', color: 'teal.6' },
            ]}
            tickLine="y"
        />
    </div>
  );
}
