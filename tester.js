var data_from = {{ my_data }}

<div class="cd-filter-block">
  <h4 class="closed">Select</h4>
  <div class="cd-filter-content" style="display: none;">
    <div class="cd-select cd-filters">
      <select class="filter" name="selectThis" id="selectThis">
        <option value="">Choose an option</option>
        <option value=".option1">Option 1</option>
        <option value=".option2">Option 2</option>
        <option value=".option3">Option 3</option>
        <option value=".option4">Option 4</option>
      </select>
    </div> <!-- cd-select -->
  </div> <!-- cd-filter-content -->
</div>

<div class="cd-filter-block">
  <h4 class="">Select</h4>
  <div class="cd-filter-content" style="display: block;">
    <div class="cd-select cd-filters">
      <select class="filter" name="selectThis" id="selectThis">
        <option value="">Choose an option</option>
        <option value=".option1">Option 1</option>
        <option value=".option2">Option 2</option>
        <option value=".option3">Option 3</option>
        <option value=".option4">Option 4</option>
      </select>
    </div> <!-- cd-select -->
  </div> <!-- cd-filter-content -->
</div>


<div class="cd-filter-block">
  <h4 class="">Check boxes</h4>
  <ul class="cd-filter-content cd-filters list" style="display: block;">
    <li>
      <input class="filter" data-filter=".check1" type="checkbox" id="checkbox1">
      <label class="checkbox-label" for="checkbox1">Option 1</label>
    </li>
    <li>
			<input class="filter" data-filter=".check2" type="checkbox" id="checkbox2">
			<label class="checkbox-label" for="checkbox2">Option 2</label>
		</li>
		<li>
			<input class="filter" data-filter=".check3" type="checkbox" id="checkbox3">
			<label class="checkbox-label" for="checkbox3">Option 3</label>
		</li>
	</ul> <!-- cd-filter-content -->
</div>

<div class="cd-filter-block">
  <h4 class="closed">Check boxes</h4>
  <ul class="cd-filter-content cd-filters list" style="display: none;">
    <li>
      <input class="filter" data-filter=".check1" type="checkbox" id="checkbox1">
      <label class="checkbox-label" for="checkbox1">Option 1</label>
    </li>
    <li>
    	<input class="filter" data-filter=".check2" type="checkbox" id="checkbox2">
    	<label class="checkbox-label" for="checkbox2">Option 2</label>
    </li>
    <li>
    	<input class="filter" data-filter=".check3" type="checkbox" id="checkbox3">
    	<label class="checkbox-label" for="checkbox3">Option 3</label>
    </li>
  </ul> <!-- cd-filter-content -->
</div>
