<template>
	<view>
		<form @submit="submitInformation">
			<view class='input-group'>
				<view class='input'>
					名字：<input name='name' placeholder="输入名字" />
				</view>
				<view class='input'>
					用户编号：<input name='userID' placeholder="输入用户编号" />
				</view>
				<view class='input'>
					用户住址：<input name='address' placeholder="输入用户住址" />
				</view>
				<view class='input'>
					手机号：<input name='telephone' placeholder="用户手机号" />
				</view>
				<view class='input'>
					经度：<input name='longitude' :value="longitude" placeholder="输入经度" ></input>
				</view>
				<view class='input'>
					纬度：<input name='latitude' :value="latitude" placeholder="输入纬度" ></input>
				</view>
				<button  @click="getlocation">获取当前位置</button>
			</view>
			<view>
				<button form-type="submit" type="primary">提交</button>
			</view>
		</form>
	</view>
</template>

<script>
	var  r=/^1[3|4|5|8][0-9]\d{4,8}$/;
	var _self;
	export default{
		data(){
			return{
				longitude:'',
				latitude:'',
			}
		},
		methods:{
			getlocation:function(){
				_self=this;
				uni.getLocation({
					success: function (res) {
						_self.longitude=res.longitude;
						_self.latitude=res.latitude;
					        //console.log('当前位置的经度：' + res.longitude);
					        //console.log('当前位置的纬度：' + res.latitude);
					    }
				})
			},
			submitInformation:function(e){
				
				if(e.detail.value.name==''){
					uni.showToast({
						icon:'none',
						title:'未填写姓名'
					})
				}
				else if(e.detail.value.userID==''){
					uni.showToast({
						icon:'none',
						title:'用户编号'
					})
				}
				
				else if(e.detail.value.address==''){
					uni.showToast({
						icon:'none',
						title:'未填写地址'
					})
				}
				
				else if(!r.test(e.detail.value.telephone)){
					uni.showToast({
						icon:'none',
						title:'手机号不合法'
					})
				}
				else if(e.detail.value.longitude==''|| isNaN(e.detail.value.longitude)){
					uni.showToast({
						icon:'none',
						title:'经度不合法'
					})
				}
				else if(e.detail.value.latitude=='' || isNaN(e.detail.value.latitude)){
					uni.showToast({
						icon:'none',
						title:'纬度不合法'
					})
				}
	
				
				else{
					console.log('form发生了submit事件，携带数据为：' + JSON.stringify(e.detail.value))
					var formdata = e.detail.value;
					uni.request({
						url:'http://182.92.239.229/user',
						data:e.detail.value,
						success: (res) => {
							console.log(res.data);
							if(res.data=='True'){
								uni.showToast({
									icon:'none',
									title:'添加成功'
								});
								
								setTimeout(function(){uni.navigateBack()},1000)
										
							}
							else{
								uni.showToast({
									icon:'none',
									title:'已有此编号'
								})
							}
						}
					})
					// uni.showModal({
					// 	content: '表单数据内容：' + JSON.stringify(formdata),
					// 	showCancel: false,
						
					// });
				}
			}
		}
	}
</script>

<style>
	.input{
		display: flex;
		margin: 30rpx;
		border-bottom: solid 1rpx #C8C7CC;
		
	}
	.picker{
		display: flex;
		margin: 30rpx;
		border-bottom: solid 1rpx #C8C7CC;
		
	}
</style>
