// Ways to follow the site (Mark's mom, 10/21: "a way to sign up to receive a notification when a new article
// has been published"). The feed is /rss.xml (src/pages/rss.xml.js); the email list is a Buttondown newsletter
// that watches that feed and sends one email per new article. Set BUTTONDOWN to the Buttondown username and
// the signup form appears in the footer and at the end of every article; empty, the pages show the feed only.
export const BUTTONDOWN = '';
export const FEED = '/rss.xml';
export const subscribeAction = () => BUTTONDOWN ? `https://buttondown.com/api/emails/embed-subscribe/${BUTTONDOWN}` : null;
