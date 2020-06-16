<template>
	<view>
		<button type="primary" class="button" @tap="addStaffs">添加员工</button>
		<button type="primary" class="button" @tap="changeStaffsInformation">修改员工信息</button>
		<button type="primary" class="button" @tap="deleteStaffs">删除员工</button>
	</view>

</template>

<script>
	export default{
		data(){
			return {
				
			}
		},
			
		methods:{
			addStaffs:function(){
				uni.navigateTo({
					url:'addStaffs/addStaffs'
				})
			},
			changeStaffsInformation:function(){
				uni.navigateTo({
					url:'changeStaffsInformation/changeStaffsInformation'
				})
			},
			deleteStaffs:function(){
				uni.navigateTo({
					url:'deleteStaffs/deleteStaffs'
				})
			}
		}
		
	}
</script>

<style>
	.button{
		margin: 100rpx;
		
	}
</style>
