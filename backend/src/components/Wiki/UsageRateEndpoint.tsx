import { useState } from "react";
import { NativeSelect } from "@mantine/core";
import { CodeHighlight } from "@mantine/code-highlight";

export function UsageRateEndpoint() {
  const [date, setDate] = useState("2024-01");

  return (
    <>
      <NativeSelect
        description="Date"
        data={[
          { label: "Jan 2024", value: "2024-01" },
          { label: "Dec 2023", value: "2023-12" },
          { label: "Nov 2023", value: "2023-11" },
          { label: "Oct 2023", value: "2023-10" },
          { label: "Sep 2023", value: "2023-09" },
          { label: "Aug 2023", value: "2023-08" },
          { label: "Jul 2023", value: "2023-07" },
          { label: "Jun 2023", value: "2023-06" },
          { label: "May 2023", value: "2023-05" },
          { label: "Apr 2023", value: "2023-04" },
          { label: "Mar 2023", value: "2023-03" },
          { label: "Feb 2023", value: "2023-02" },
          { label: "Jan 2023", value: "2023-01" },
        ]}
        value={date}
        onChange={(event) => setDate(event.currentTarget.value)}
      />
      <br />
      <CodeHighlight
        language="bash"
        code={`/api/usage-rate?pokemon=GreatTusk&date=${date}`}
      />
    </>
  );
}
