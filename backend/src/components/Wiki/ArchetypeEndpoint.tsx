import { useState } from "react";
import { NativeSelect } from "@mantine/core";
import { CodeHighlight } from "@mantine/code-highlight";

export function ArchetypeEndpoint() {
  const [archetype, setArchetype] = useState("ho");

  return (
    <>
      <NativeSelect
        description="Possible Archetypes"
        data={[
          { label: "Hyper Offense", value: "ho" },
          { label: "Stall", value: "stall" },
          { label: "Bulky Offense", value: "bo" },
          { label: "Balance", value: "balance" },
          { label: "Weather", value: "weather" },
        ]}
        value={archetype}
        onChange={(event) => setArchetype(event.currentTarget.value)}
      />
      <br />
      <CodeHighlight
        language="bash"
        code={`/api/teambuilder?archetype=${archetype}`}
      />
    </>
  );
}
