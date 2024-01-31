import React from "react";
import classes from "./Mdx.module.css";

interface MdxPageProps {
  children: React.ReactNode;
}

export function MdxPage({ children }: MdxPageProps) {
  return (
    <>
      <div className={classes.wrapper}>
        <div className={classes.container}>{children}</div>
      </div>
    </>
  );
}
