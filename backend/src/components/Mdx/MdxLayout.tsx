import React from "react";
import { MdxPage } from "@/components/Mdx/MdxPage";

export function Layout() {
  return ({ children }: { children: React.ReactNode }) => (
    <MdxPage>{children}</MdxPage>
  );
}
