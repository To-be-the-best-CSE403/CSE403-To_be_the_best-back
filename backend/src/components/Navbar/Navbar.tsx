"use client";

import { ScrollArea } from "@mantine/core";

import { NavItem } from "@/types/nav-item";
import classes from "./Navbar.module.css";
import { NavLinksGroup } from "./NavLinksGroup";

interface Props {
  data: NavItem[];
  hidden?: boolean;
}

export function Navbar({ data }: Props) {
  const links = data.map((item) => (
    <NavLinksGroup key={item.label} {...item} />
  ));

  return (
    <>
      <ScrollArea className={classes.links}>
        <div className={classes.linksInner}>{links}</div>
      </ScrollArea>
    </>
  );
}
