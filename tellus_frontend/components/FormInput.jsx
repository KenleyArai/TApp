import React from "react";

const FormInput = ({ title, value, onChange }) => {
  return (
    <label>
      {title}:
      <input
        type="text"
        value={value}
        onChange={e => onChange(e.target.value)}
        required
      />
    </label>
  );
};

export default FormInput;
