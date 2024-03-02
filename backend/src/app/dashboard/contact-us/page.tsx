"use client";

import React from "react";
import ContactForm from "../../../components/Contact-Form/contact-form";
import ContactUsMdx from "./contact-us.mdx";

export default function ContactUs() {
    return (
        <div>
            <ContactUsMdx/>
            <ContactForm />
        </div>
    );
}
