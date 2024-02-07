"use client";

import React from "react";
import ArchtypeTeam1Mdx from "./archetype-team1.mdx";
import ArchtypeTeam2Mdx from "./archetype-team2.mdx";
import { Autocomplete } from '@mantine/core'; {/* Mantine Core/ComboBox/Autocomplete/Group Options*/}

export default function ArchtypeTeam() {
  return (
    <div>
      <ArchtypeTeam1Mdx />
      <Autocomplete
      label="Archetypes in Pokémon Showdown"
      placeholder="Pick an archetype or enter anything"
      data={[
        { group: 'Format 1', items: ['Archetype 1', 'Archetype 2'] },
        { group: 'Format 2', items: ['Archetype 3', 'Archetype 4'] },
      ]}
    />
    <ArchtypeTeam2Mdx />
    </div>
  );
}
