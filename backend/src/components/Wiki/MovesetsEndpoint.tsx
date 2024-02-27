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
                    { label: "Great Tusk", value: "greattusk" },
                    { label: "Kingambit", value: "kingambit" },
                    { label: "Gholdengo", value: "gholdengo" },
                    { label: "Raging Bolt", value: "ragingbolt" },
                    { label: "Gliscor", value: "gliscor" },
                    { label: "Volcarona", value: "volcarona" },
                    { label: "Dragapult", value: "dragapult" },
                    { label: "Iron Valiant", value: "ironvaliant" },
                    { label: "Roaring Moon", value: "roaringmoon" },
                    { label: "Hatterene", value: "hatterene" }
                ]}
                value={pokemon}
                onChange={(event) => setPokemon(event.currentTarget.value)}
            />
            <br />
            <CodeHighlight
                language="bash"
                code={`/api/movesets?pokemon=${pokemon}`}
            />
        </>
    );
}
