<template>
	<view class='content'>
		<view class="btn-row">

				<button type="primary" class="primary"  @tap="check" :disabled="staffIsAble">进行检查</button>
				
				<button type="primary" class="primary"  @tap="staffManagement" :disabled="managerIsAble">员工管理</button>
				<button type="primary" class="primary"  @tap="userManagement" :disabled="managerIsAble">用户管理</button>
				<button type="primary" class="primary"  @tap="getcheckrecords" :disabled="managerIsAble">查看检查记录</button>
				
		</view>
	</view>
</template>

<script>
	var _user;
	
	export default{
		
		data() {
			return {
				staffIsAble: true,
				managerIsAble:true,
				usertype:''
			}
			
		},
		

		
		methods:{
			onLoad() {
				_user=this;
				_user.usertype=uni.getStorageSync('usertype');
				
				if( _user.usertype==1 ){//条件内调用methods判断是什么登陆类型
					_user.staffIsAble=false;

				}
				else if(_user.usertype==2){
					_user.managerIsAble=false;
				}
				
			},

			check:function(){
				uni.navigateTo({
					url:'../customersList/customersList'
				})
				
			},
			staffManagement:function(){
				uni.navigateTo({
					url:'../staffManagement/staffManagement'
				})
			},
			userManagement:function(){
				uni.navigateTo({
					url:'../customerManagement/customerManagement'
				})
			},
			getcheckrecords:function(){
				uni.navigateTo({
					url:'../getcheckrecords/getcheckrecords'
				})
			},
		}
		
	}

	
</script>

<style>
	.content {
		display: block;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.primary{
		margin: 100rpx;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}
</style>
