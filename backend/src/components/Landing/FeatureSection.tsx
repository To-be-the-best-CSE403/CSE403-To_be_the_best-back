"use client";

import {
  Container,
  Paper,
  SimpleGrid,
  Text,
  ThemeIcon,
  Title,
} from "@mantine/core";
import {
  IconPokeball,
  IconGauge,
  IconDeviceAnalytics,
} from "@tabler/icons-react";
import classes from "./FeatureSection.module.css";

export const featuresData = [
  {
    icon: IconPokeball,
    title: "Team Builder",
    description:
      "Build winning Pokémon teams with access to common movesets, usage stats, and archetype-based team creation.",
  },
  {
    icon: IconGauge,
    title: "In-depth Statistics",
    description:
      "Access detailed statistics for each Pokémon, including usage rate, win rate and build popularity.",
  },
  {
    icon: IconDeviceAnalytics,
    title: "Battle Analysis",
    description:
      "Enhance your battle strategy with damage prediction and real-time battle move suggestions.",
  },
];

interface FeatureProps {
  icon: React.FC<any>;
  title: React.ReactNode;
  description: React.ReactNode;
}

export function Feature({ icon: Icon, title, description }: FeatureProps) {
  return (
    <Paper h="100%" shadow="md" px="lg" py="sm" radius="md" withBorder>
      <ThemeIcon variant="light" size={60} radius={60}>
        <Icon size="2rem" stroke={1.5} />
      </ThemeIcon>
      <Text mt="sm" mb={7} fw="600">
        {title}
      </Text>
      <Text size="sm" c="dimmed" style={{ lineHeight: 1.6 }}>
        {description}
      </Text>
    </Paper>
  );
}

interface FeatureGridProps {
  title: React.ReactNode;
  data?: FeatureProps[];
}

export function FeatureSection({
  title,
  data = featuresData,
}: FeatureGridProps) {
  const features = data.map((feature, index) => (
    <Feature {...feature} key={index} />
  ));

  return (
    <Container className={classes.wrapper}>
      <Title className={classes.title}>{title}</Title>

      <SimpleGrid
        mt={30}
        cols={{ base: 1, sm: 2, lg: 3 }}
        spacing={{ base: "lg", md: "lg", lg: "xl" }}
      >
        {features}
      </SimpleGrid>
    </Container>
  );
}
