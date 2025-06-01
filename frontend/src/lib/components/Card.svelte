<script>
	let { status, name, url } = $props();

	let copied = $state(false);

	function copyToClipboard() {
		navigator.clipboard
			.writeText('cloudflared access tcp --hostname ' + url + ' --url localhost:5432')
			.then(() => {
				copied = true;
				setTimeout(() => (copied = false), 2000);
			});
	}
</script>

<div class="relative mx-auto w-full max-w-sm rounded-lg bg-[#272727] p-4 shadow-md">
	<h3 class="text-lg font-bold text-white uppercase">{name}</h3>
	<p class="mt-2">
		<span
			class="inline-block rounded px-2 py-1 text-sm font-semibold
      {status === 'running'
				? 'bg-green-100 text-green-800'
				: status === 'exited'
					? 'bg-red-100 text-red-800'
					: 'bg-gray-100 text-gray-800'}"
		>
			{status}
		</span>
	</p>
	<p class="mt-2 font-mono text-sm break-all text-gray-200">
		cloudflared access tcp--hostname {url} --url localhost:5432
	</p>
	<button
		onclick={copyToClipboard}
		class="mt-2 rounded bg-blue-500 px-3 py-1 text-sm text-white hover:bg-blue-600"
	>
		Copy URL
	</button>
	{#if copied}
		<span class="absolute top-2 right-2 rounded bg-gray-800 px-2 py-1 text-xs text-white">
			Copied!
		</span>
	{/if}
</div>
