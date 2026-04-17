import ButtonComp from "./component/button";
import CheckboxComp from "./component/checkbox";
import RatingComp from "./component/Rating";
import SelectComp from "./component/select";
import TextFieldComp from "./component/textfield";

function App() {
  return (
    <div style={{ padding: 40, maxWidth: 500 }}>
      <h2>Experiment 2 – UI using Component Libraries</h2>

      <ButtonComp /><br /><br />
      <CheckboxComp /><br /><br />
      <RatingComp /><br /><br />
      <SelectComp /><br /><br />
      <TextFieldComp />
    </div>
  );
}

export default App;
