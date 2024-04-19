<script>
	import { page } from '$app/stores';
	let Page;
	$: Page = $page.url.pathname;
</script>

<div class="ui fixed inverted menu">
	<div class="ui container">
		<a href="/" class="header item">
			<img class="logo" src="assets/images/logo.png" alt="Dictionary Logo"/>
			Dictionary
		</a>
		<a href="/" class={Page === '/' ? 'active item' : 'item'}>Home</a>
		<a href="/lookup" class={Page === '/lookup' ? 'active item' : 'item'}>Lookup</a>
		<a href="/about" class={Page === '/about' ? 'active item' : 'item'}>About</a>
	</div>
</div>
