<template>
	<view>
		<button type="primary" class="button" @tap="addUsers">添加用户</button>
		<button type="primary" class="button" @tap="changeUsersInformation">修改用户信息</button>
		<button type="primary" class="button" @tap="deleteUsers">删除用户</button>
	</view>

</template>

<script>
	export default{
		data(){
			return {
				
			}
		},
			
		methods:{
			addUsers:function(){
				uni.navigateTo({
					url:'addUsers/addUsers'
				})
			},
			changeUsersInformation:function(){
				uni.navigateTo({
					url:'changeUsersInformation/changeUsersInformation'
				})
			},
			deleteUsers:function(){
				uni.navigateTo({
					url:'deleteUsers/deleteUsers'
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
