"use client";

import React from "react";
import ContactUsMdx from "./contact-us.mdx";

export default function ContactUs() {
    return (
        <div>
            <div dangerouslySetInnerHTML={{__html: ContactUsMdx}} />
        </div>
    );
}
