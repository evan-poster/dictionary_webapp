<script>
	import Navbar from '../components/Navbar.svelte';
</script>

<Navbar />

<div class="ui main text container">
	<slot />
</div>

<style>
	.ui.main.text.container {
		margin-top: 5em;
	}
</style>