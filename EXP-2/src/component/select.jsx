import { Select, MenuItem } from "@mui/material";

export default function SelectComp() {
  return (
    <Select defaultValue="">
      <MenuItem value="">None</MenuItem>
      <MenuItem value={1}>One</MenuItem>
      <MenuItem value={2}>Two</MenuItem>
    </Select>
  );
}
