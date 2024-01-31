"use client";

import { Button, Container, Group, Text, Title } from "@mantine/core";
import { IconArrowRight, IconStar } from "@tabler/icons-react";
import { useRouter } from "next/navigation";
import classes from "./HeroSection.module.css";

export function HeroSection() {
  const router = useRouter();

  return (
    <Container pt="sm" size="lg">
      <div className={classes.inner}>
        <Title className={classes.title}>ToBeTheBest</Title>
        <Title className={classes.subtitle}>
          Your Pokemon Showdown Strategy Ally
        </Title>

        <Text className={classes.description} mt={30}>
          Build winning teams and master battles with ToBeTheBest. Get move
          suggestions, usage stats, and more, all in one handy extension.
        </Text>

        <Group mt={40}>
          <Button
            size="lg"
            className={classes.control}
            onClick={() => {
              router.push("/dashboard/getting-started");
            }}
            rightSection={<IconArrowRight />}
          >
            Get started
          </Button>
          <Button
            variant="outline"
            size="lg"
            className={classes.control}
            onClick={() => {
              // open github
              window.open(
                "https://github.com/To-be-the-best-CSE403/CSE403-To_be_the_best-front"
              );
            }}
            rightSection={<IconStar />}
          >
            Github
          </Button>
        </Group>
      </div>
    </Container>
  );
}
