<h1>All Words</h1>


<script context="module">
	import { page } from '@sveltejs/kit'
	import { paginate } from 'svelte-paginate'
	export const load = async ({ params }) => {
		const response = await page({
			endpoint: `/api/words/letter/${params.letter}`
		})
		const words = await response.json()
		return {
			words: paginate(words, { limit: 10, sort: (a, b) => a.text.localeCompare(b.text) })
		}
	}
</script>

<script>
	export let words
</script>

<ul>
	{#each $paginate.items as word}
		<li>{word.text}</li>
	{/each}
</ul>

<div class="svelte-paginate-pagination">
	{$paginate.links({
		first: 'First',
		last: 'Last',
		prev: 'Prev',
		next: 'Next'
	})}
</div>
