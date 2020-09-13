import {extend} from "vee-validate";
import {email, required, min} from "vee-validate/dist/rules";
// import { ValidationMessageTemplate } from 'vee-validate'

extend("required", {
  ...required,
  message: "Palun täitke antud väli"});

extend("email", {
  ...email,
  message: "Ebakorrektne email",
});

extend("duplicate", {
  params: ["target"],
  validate(value, { target }) {
    return value === target;
  },
  message: "Paroolid ei klappi",
});

extend("min", {
  ...min,
  message: "Vähemalt X tähemärki",
});

extend('min', {
  validate(value, args) {
    return value.length >= args.length;
  },
  params: ['length'],
  message: "Vähemalt {length} tähemärki",
});

//
// extend("min", {
//   ...min,
//   message: "Vähemalt X tähemärki",
// });

// extend("password", {
//   validate: (value) => {
//     const strongPasswordRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})");
//     return strongPasswordRegex.test(value);
//   },
// });
