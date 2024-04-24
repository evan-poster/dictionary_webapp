<script>
	import { page } from '$app/stores';
	let Page;
	$: Page = $page.url.pathname;
</script>

<div class="ui fixed inverted menu">
	<div class="ui container">
		<a href="/" class="header item">
			<img class="logo" src="/images/logo.png" alt="Dictionary Logo"/>
			Dictionary
		</a>
		<a href="/" class={Page === '/' ? 'active item' : 'item'}>Home</a>
		<a href="/lookup" class={Page === '/lookup' ? 'active item' : 'item'}>Lookup</a>
		<a href="/all" class={Page === '/all' ? 'active item' : 'item'}>All Words</a>
		<a href="/about" class={Page === '/about' ? 'active item' : 'item'}>About</a>
	</div>
</div>
