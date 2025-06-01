<script>
  let copied = '';

  function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
      copied = text;
      setTimeout(() => (copied = ''), 2000);
    });
  }
</script>

	<nav class="bg-gray-800 shadow-lg">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-16 justify-between">
				<div class="flex items-center">
					<a href="/" class="text-2xl font-bold text-indigo-400"
						>TYSONCLOUD 
					</a>
            <span
							style="border-radius: 1000px; color: var(--color-indigo-400); border: 2px solid
              var(--color-indigo-400); padding: 0 8px; margin-left: 10px;" class="text-[16px]">demo</span
						>
				</div>
				<div class="flex items-center">
					<form action="?/logout" method="post">
					<button
						class="rounded-md bg-indigo-600 px-4 py-2 text-sm font-semibold text-white transition duration-200 hover:bg-indigo-700"
					>
						Log Out
					</button>
          </form>
				</div>
			</div>
		</div>
	</nav>
<div class="container mx-auto p-4 max-w-3xl">
  <h1 class="text-2xl font-bold text-white mb-6">Install Dependencies</h1>

  <!-- Cloudflared -->
  <div class="mb-6">
    <h2 class="text-lg font-semibold text-white mb-2">Cloudflared</h2>
    <div class="bg-gray-700 shadow rounded p-4 mb-2 relative">
      <p class="text-sm text-white mb-1">This command is for macOS users</p>
      <p class="font-mono text-sm bg-gray-600 text-white p-2 rounded">brew install cloudflared</p>
      <button
        on:click={() => copyToClipboard('brew install cloudflared')}
        class="absolute top-2 right-2 bg-blue-500 hover:bg-blue-600 text-white px-2 py-1 rounded text-xs">
        Copy
      </button>
      {#if copied === 'brew install cloudflared'}
        <span class="absolute top-2 right-2 bg-gray-800 text-white text-xs px-2 py-1 rounded">Copied!</span>
      {/if}
    </div>
    <div class="bg-gray-700 shadow rounded p-4 relative">
      <p class="text-sm text-white mb-1">This command is for Windows users</p>
      <p class="font-mono text-sm bg-gray-600 text-white p-2 rounded">winget install --id Cloudflare.cloudflared</p>
      <button
        on:click={() => copyToClipboard('winget install --id Cloudflare.cloudflared')}
        class="absolute top-2 right-2 bg-blue-500 hover:bg-blue-600 text-white px-2 py-1 rounded text-xs">
        Copy
      </button>
      {#if copied === 'winget install --id Cloudflare.cloudflared'}
        <span class="absolute top-2 right-2 bg-gray-800 text-white text-xs px-2 py-1 rounded">Copied!</span>
      {/if}
    </div>
  </div>

  <!-- psql -->
  <div>
    <h2 class="text-lg font-semibold text-white mb-2">psql (PostgreSQL Client)</h2>
    <div class="bg-gray-700 shadow rounded p-4 mb-2 relative">
      <p class="text-sm text-white mb-1">This command is for macOS users</p>
      <p class="font-mono text-sm bg-gray-600 text-white p-2 rounded">brew install postgresql</p>
      <button
        on:click={() => copyToClipboard('brew install postgresql')}
        class="absolute top-2 right-2 bg-blue-500 hover:bg-blue-600 text-white px-2 py-1 rounded text-xs">
        Copy
      </button>
      {#if copied === 'brew install postgresql'}
        <span class="absolute top-2 right-2 bg-gray-800 text-white text-xs px-2 py-1 rounded">Copied!</span>
      {/if}
    </div>
    <div class="bg-gray-700 shadow rounded p-4 relative">
      <p class="text-sm text-white mb-1">Windows Installer</p>
      <a href="https://sbp.enterprisedb.com/getfile.jsp?fileid=1259563" class="font-mono text-sm bg-gray-600 text-white p-2 rounded">https://sbp.enterprisedb.com/getfile.jsp?fileid=1259563</a>
    </div>
  </div>
</div>
