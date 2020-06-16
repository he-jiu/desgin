<template>
	<view class="content">
		<image src="../../static/img/qq.png" class='image' @tap="changeImage"></image>
		<view  class='message'>
			<view class='text'>姓名：{{name}}</view>
			<view class='text'>编号：{{number}}</view>
			<view class='text'>工种：{{usertype}}</view>
		</view>
		<view class="btn-row">
			<button class="logout" @tap="logout">退出登录</button>
		</view>	
		<view class="action-row">
			<navigator url="../pwd/pwd">修改密码</navigator>
		</view>
	</view>
</template>


<script>
	
	
	var _user;
		
	export default{
		
		data(){
			return{
				name:'',
				number:'',
				usertype:'',
				}
		},

		
		
		
		methods:{
			onLoad:function(){
				
				this.name=uni.getStorageSync('name');
				this.number=uni.getStorageSync('number');
				this.usertype=uni.getStorageSync('usertype');
				if(this.usertype==1){
					this.usertype='操作员'
				}
				if(this.usertype==2){
					this.usertype=='管理员'
				}
				
				
			},
			
			
						
			logout:function(){
				uni.reLaunch({
					url:'../login/login'
				})

			}
		}
		
	} 


			

</script>
	

<style>
	.image{
		width: 200rpx;
		height: 200rpx;
		margin-left:275rpx;
		margin-top:100rpx;
	}
	.message{
		margin-top: 100rpx;
		margin-left: 100rpx;
	}
	.text{
		margin: 50rpx;
	}
	.logout{
		margin: 30rpx;
		background-color: #0faeff;
		color: #FFFFFF;
	}
	.action-row{
		margin-left:300rpx;
	}
	
</style>
