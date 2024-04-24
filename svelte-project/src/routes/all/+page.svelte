<h1>All Worlds</h1>

<div class="ui three column doubling stackable grid">
  {#each Array.from({ length: 26 }, (_, i) => String.fromCharCode(i + 97)) as letter}
    <div class="column">
      <a href={`/all/${letter.toLowerCase()}`} class="ui button">{letter}</a>
    </div>
  {/each}
</div>
