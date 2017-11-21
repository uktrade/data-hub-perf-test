Perf testing for data hub
====

Currently this requires two env vars to start. A COOKIE from a current valid user session and a TARGET that is the system to test.

Keep an eye on returned file sizes. If they are all the same then you've hit the SSO login page and you'll need a new cookie. You may also see 502s in the error list.