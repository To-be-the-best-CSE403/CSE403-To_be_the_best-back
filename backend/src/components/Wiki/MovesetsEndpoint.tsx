import { useState } from "react";
import { NativeSelect } from "@mantine/core";
import { CodeHighlight } from "@mantine/code-highlight";

export function MovesetsEndpoint() {
    const [pokemon, setPokemon] = useState("greattusk");

    return (
        <>
            <NativeSelect
                description="Top 10 Pokemon"
                data={[
                    { label: "Great Tusk", value: "gt" },
                    { label: "Kingambit", value: "king" },
                    { label: "Gholdengo", value: "ghold" },
                    { label: "Raging Bolt", value: "rb" },
                    { label: "Gliscor", value: "glis" },
                    { label: "Volcarona", value: "volc" },
                    { label: "Dragapult", value: "drag" },
                    { label: "Iron Valiant", value: "iv" },
                    { label: "Roaring Moon", value: "rm" },
                    { label: "Hatterene", value: "hatt" }
                ]}
                value={pokemon}
                onChange={(event) => setPokemon(event.currentTarget.value)}
            />
            <br />
            <CodeHighlight
                language="bash"
                code={`/api/movesets?archetype=${pokemon}`}
            />
        </>
    );
}
