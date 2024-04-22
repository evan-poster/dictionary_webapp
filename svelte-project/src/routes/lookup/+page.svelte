<h1>Lookup Word:</h1>

<div class="ui grid">
  <div class="row">
    <div class="ten wide column">
      <form class="ui form" on:submit|preventDefault={search}>
        <div class="field">
          <div class="ui icon input">
            <input type="text" placeholder="Enter a word" bind:value={searchTerm}>
            <i class="search icon"></i>
          </div>
        </div>
      </form>
    </div>
  </div>
  {#if result}
  <div class="row">
    <div class="ten wide column">
      <div class="ui items">
        <div class="item">
          <div class="content">
            <div class="header">{result.word}</div>
            <!-- Loopo through definitions and display them -->
            {#each result.definitions as definition}
            <div class="description">{definition.part_of_speech}</div>
            <div class="description">{definition.definition}</div>
            {/each}
          </div>
        </div>
      </div>
    </div>
  </div>
  {/if}
  {#if !result}
  <div class="row">
    <div class="ten wide column">
      <div class="ui items">
        <div class="item">
          <div class="content">
            <div class="header">No results found</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  {/if}
</div>

<script>
  export let result = null;
  let searchTerm = '';

  function search() {
    console.log("Searching for ${searchTerm}");
    const url = `http://127.0.0.1:8000/word/${searchTerm}`;
    fetch(url)
      .then(resp => resp.json())
      .then(data => result = data)
  }
</script>

<style>
  .ui.form {
    margin-top: 1em;
  }

  .ui.items {
    margin-top: 1em;
  }
</style>

