import { useForm, ValidationError } from "@formspree/react";

export default function ContactForm() {
    const [state, handleSubmit] = useForm("mzbngodg");

    if (state.succeeded) {
        return <p>Thanks for your submission!</p>;
    }

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="email">Email Address</label>
            <div>
                <input id="email" type="email" name="email" size="30"/>
                <ValidationError prefix="Email" field="email" errors={state.errors} />
            </div>
            <div>
                <label htmlFor="message">Message</label>
                <textarea id="message" name="message" rows="10" cols="50" />
                <ValidationError prefix="Message" field="message" errors={state.errors} />
            </div>
            <div>
                <button type="submit" disabled={state.submitting}>
                    Submit
                </button>
                <ValidationError errors={state.errors} />
            </div>
        </form>
    );
}