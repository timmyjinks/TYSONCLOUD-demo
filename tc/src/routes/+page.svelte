<script lang="ts">
	import Card from '$lib/components/Card.svelte';
	export let data;
</script>

<div class="flex min-h-screen flex-col">
	<nav class="bg-gray-800 shadow-lg">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-16 justify-between">
				<div class="flex items-center">
					<span class="text-2xl font-bold text-indigo-400"
						>TYSONCLOUD <span
							style="border-radius: 1000px; color: var(--color-indigo-400); border: 2px solid
              var(--color-indigo-400); padding: 0 8px; margin-left: 10px">demo</span
						>
					</span>
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
	<div class="flex items-center justify-center px-4 py-8 text-white">
		<div class="w-[100%] text-center">
			<h1 class="mb-4 text-4xl font-bold">Welcome back {data.user?.username}!</h1>
			{#if data.databases.length == 0}
				<p class="mb-6 text-lg text-gray-300">
					Create and manage your PostgreSQL databases with ease. Get started by creating your first
					database!
				</p>
				<div class="flex justify-center">
					<a href="/create">
						<div class="rounded-lg bg-gray-800 p-6 shadow-lg">
							<h2 class="mb-2 text-xl font-semibold">Create Database</h2>
							<p class="text-gray-400">Spin up a new PostgreSQL instance in seconds.</p>
						</div>
					</a>
				</div>
			{:else}
				<div class="flex">
					<div class="rows-auto grid w-[100%] grid-cols-4 gap-5">
						{#each data.databases as database}
							<Card name={database.name} status={database.status} />
						{/each}
						<a
							href="/create"
							class="m-[15px] flex items-center justify-center rounded-lg bg-[#272727] p-[10px]"
						>
							<div class="">
								<h2 class="rounded-lg text-[50px]">+</h2>
							</div>
						</a>
					</div>
				</div>
			{/if}
		</div>
	</div>
</div>
