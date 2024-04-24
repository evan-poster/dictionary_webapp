<script>
	export let result = null;
	let searchTerm = '';

	function search() {
		console.log('Searching for ${searchTerm}');
		const url = `http://127.0.0.1:8000/api/word/${searchTerm}`;
		fetch(url)
			.then((resp) => resp.json())
			.then((data) => (result = data));
	}
</script>

<style>
	.ui.form {
		margin-top: 1em;
	}

	.ui.items {
		margin-top: 1em;
	}

	@keyframes fade {
		0% {
			opacity: 0;
		}
		100% {
			opacity: 1;
		}
	}

	.fade {
		animation: fade 0.3s ease-in-out;
	}
</style>

<h1>Lookup Word:</h1>

<div class="ui grid">
	<div class="row">
		<div class="twelve wide column">
			<form class="ui form" on:submit|preventDefault={search}>
				<div class="field">
					<div class="ui icon input">
						<input type="text" placeholder="Enter a word" bind:value={searchTerm} />
						<i class="search icon"></i>
					</div>
				</div>
			</form>
		</div>
	</div>
	<!-- if we have a result and it isn't an error, display it -->
	{#if result && !result.error}
		<div class="row fade">
			<div class="twelve wide column">
				<div class="ui items">
					<div class="item">
						<div class="content">
							<div class="header">{result.word}</div>
							<!-- Loop through definitions and display them if there are multiple -->
							{#if result.definitions.length > 1}
								{#each result.definitions as definition}
									<div class="description">
										<i>{definition.part_of_speech}</i> - {definition.definition}
									</div>
								{/each}
							{/if}
							<!-- Display the definition if there is only one -->
							{#if result.definitions.length === 1}
								<div class="description">
									<i>{result.definitions[0].part_of_speech}</i> - {result.definitions[0].definition}
								</div>
							{/if}
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- If we have no results or an error, display a message -->
	{:else}
		<div class="row fade">
			<div class="twelve wide column">
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

