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
            <div class="description">{result.definition}</div>
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
    const url = `/api/lookup/${searchTerm}`;
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

