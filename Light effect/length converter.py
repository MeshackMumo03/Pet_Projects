
function LengthConverter(val) {
  var input2 = document.getElementById("meter").value = val / 3.2808;
  console.log(input2);
  val.value = input2.value;
}

<div class="container">
  <div class='ftm'>
    <label for="feet">Feet:</label><br>
    <input id="feet" type="number" placeholder="Feet" onchange="LengthConverter(this.value)">
  </div>
  <div class='ftm'>
    <label for="meter">Meter:</label><br>
    <input id="meter" type="number" placeholder="Meters">
  </div>
</div>

