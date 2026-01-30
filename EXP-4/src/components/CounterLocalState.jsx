import { useState } from "react"; 
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Stack from "@mui/material/Stack";

export default function LocalStateCounter({ cno }) {
  const [count, setCount] = useState(0);

  // Event handler functions for click Event
  const increaseCount = () => setCount(count + 1);
  const decreaseCount = () => setCount(count - 1);

  return (
    <>
      <Container maxWidth="sm">
        <Box sx={{ bgcolor: '#cfe8fc', height: '100px' }} >
          <h3>{cno} : Local State Count: {count}</h3>
          <Stack direction="row" spacing={2}>
            <Button variant="outlined" onClick={increaseCount}>
              Increase
            </Button>
            <Button variant="outlined" onClick={decreaseCount}>
              Decrease
            </Button>
          </Stack>
        </Box>
      </Container>
    </>
  );
}
