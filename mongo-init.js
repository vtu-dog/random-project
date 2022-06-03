/* eslint-disable no-undef */
db.createUser({
  user: "root",
  pwd: "secret",
  roles: [
    {
      role: "readWrite",
      db: "project",
    },
  ],
});
