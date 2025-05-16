<script lang="ts">
	let { status, name } = $props();
</script>

<div class="m-[15px] rounded-lg bg-[#272727] p-[10px]">
	<h2 class="text-[18px]">{name}</h2>
	<br />
	<p>Status: {status}</p>
</div>
